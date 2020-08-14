package ca.pitt.api.quarkus.test;

import javax.ws.rs.GET;
import javax.ws.rs.Path;

/**
 * A JAX-RS interface.  An implementation of this interface must be provided.
 */
@Path("/stuff")
public interface StuffResource {
  @GET
  void get();
}
